
module.exports = function(gulp) {

  gulp.task('watch', ['connect', 'test', 'jshint'], function() {
    gulp.watch('./src/style/**/*.scss', ['styles']);
    gulp.watch('./src/apps/**/*.{js,map}', ['scripts', 'test']);
    gulp.watch('./src/apps/**/*.jade', ['templates']);
    gulp.watch(['./src/style/fonts/**/*'], ['copy']);
    gulp.watch('./src/img/**/*.{png,gif,jpg,jpeg,svg}', ['images']);
    gulp.watch('./src/icons/**/*.{png,ico,xml}');
    gulp.watch(['./src/apps/**/*.js',
                './src/test/**/*Spec.js',
                './src/test-main.js'], ['scripts', 'test']);
  });

};
