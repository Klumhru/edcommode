
module.exports = function(gulp) {

  gulp.task('build', ['bower'], function() {
    return gulp
        .start('scripts',
               'styles',
               'templates',
               'images',
               'icons',
               'copy');
  });

};
