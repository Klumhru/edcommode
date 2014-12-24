module.exports = function(gulp) {
  gulp.task('jshint', function () {
      return gulp.src(['./src/js/apps/*.js', 
                       './src/js/apps/**/*.js',
                       './src/test/**/*.js'])
              .pipe(gulp.plugin.jshint('.jshintrc'))
              .pipe(gulp.plugin.jshint.reporter('jshint-stylish'));
  });
};