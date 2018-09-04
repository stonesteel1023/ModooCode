const express = require('express');
const body_parser = require('body-parser');
const fs = require('fs');
const zmq = require('zmq');
const uuidv4 = require('uuid/v4');

const send_sock = zmq.socket('pub');
const recv_sock = zmq.socket('sub');

const app = express();

// Set the default rendering engine.
app.set('view engine', 'ejs');

// Set the static directory.
app.use(express.static(__dirname + '/../views'));
app.set('views', __dirname + '/../views');

// Set body parser.
app.use(body_parser.urlencoded({
  extended: true
}));

app.listen(80, () => console.log('The server has started.'));

app.get('/', (req, res) => res.send('Hello World!'));

fs.readFile('file_headers.json', 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  file_infos = JSON.parse(data);
  app.get("/:id", function (req, res) {
    let page_id = parseInt(req.params.id);
    if (page_id <= 228) {
      console.log(file_infos);
      res.render("page.ejs", {
        content_url: "./old/blog_" + page_id + ".html",
        file_info: file_infos[page_id]
      });
    }
  });
});

send_sock.bindSync('tcp://127.0.0.1:3001');
recv_sock.connect('tcp://127.0.0.1:3002');
recv_sock.subscribe('');

class ZmqManager {
  constructor() {
    this.requested_codes = new Map();

    recv_sock.on('message', function (message) {
      message = message.toString();
      let delimiter = message.indexOf(':');
      let next_delimiter = message.indexOf(':', delimiter + 1);

      let compile_error = '', exec_result = '';
      // There was no compile error.
      if (next_delimiter === delimiter + 1) {
        exec_result = message.substr(next_delimiter + 1);
      } else {
        compile_error = message.substr(delimiter + 1);
      }

      let id = message.substr(0, delimiter);

      console.log(id, message.substr(0, delimiter), {
        exec_result,
        compile_error
      });
      let cb = this.requested_codes.get(id);
      if (cb) {
        cb({exec_result, compile_error});
      }
    }.bind(this));
  }

  getNewId() {
    return uuidv4();
  }

  sendCodeToRun(code, stdin, cb) {
    let id = this.getNewId();
    this.requested_codes.set(id, cb);
    send_sock.send([id + ':' + stdin + id + code]);
  }
}

zmq_manager = new ZmqManager();
app.post('/run', function (req, res) {
  let code = req.body.code;
  let stdin = req.body.stdin;

  if (!stdin) {
    stdin = "";
  }

  zmq_manager.sendCodeToRun(code, stdin, function (result) {
    if (result.exec_result.length > 0) {
      console.log("Execution result : \n", result.exec_result);
    } else {
      console.log("Compile error : \n", result.compile_error)
    }
    res.send(result);
  });
});
