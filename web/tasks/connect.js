
module.exports = function(gulp) {
  var prod = gulp.plugin.util.env.prod;

  gulp.task('connect', function() {
    return gulp.plugin.connect.server({
      root: [(prod ? './dist' : './dev')],
      port: 1337,
      livereload: true,
      middleware: function(connect, o) {
        return [ (function() {
            var url = require('url');
            var proxy = require('proxy-middleware');
            var options = url.parse('http://localhost:8080/common');
            options.route = '/common';
            return proxy(options);
        })(), (function() {
            var url = require('url');
            var proxy = require('proxy-middleware');
            var options = url.parse('http://localhost:8080/api');
            options.route = '/api';
            return proxy(options);
        })() ];
      }
    });
  });
};
