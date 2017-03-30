var m2 = require('./app2');
var mysql = require('mysql');
var connection = mysql.createConncetion({
  host: 'localhost',
  user: 'davidn',
  password: 'raspberry',
  database: 'light'
});
connection.connect(function(err) {
  // connected! (unless `err` is set)
});
var _ = require('underscore');
m2();
