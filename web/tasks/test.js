module.exports = function(gulp) {
  var handleError = function (err) {
    console.log(err.name, ' in ', err.plugin, ': ', err.message);
    this.emit('end');
  };
  var karma = require('gulp-karma');
  gulp.task('test', ['jshint'], function() {
    return gulp.src(['test files are included in karma.conf.js'])
      .pipe(karma({
        configFile: 'karma.conf.js',
        action: 'run'
      }))
      .on('error', handleError);
  });
};