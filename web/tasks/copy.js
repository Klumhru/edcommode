module.exports = function (gulp) {

  gulp.task('copy', function () {
    var path = gulp.plugin.util.env.prod ? './dist' : './dev';

    gulp.src('./src/img/**/*.ico')
        .pipe(gulp.dest(path + '/img/'));
    gulp.src('./src/style/fonts/**')
        .pipe(gulp.dest(path + '/css/'));
    gulp.src('./src/videos/**')
        .pipe(gulp.dest(path + '/videos/'));

    gulp.src('./src/style/vendor/*(*.ttf|*.otf|*.woff|*.svg)')
        .pipe(gulp.dest(path + '/css/'));

    // copy resources for hradi flash component
    gulp.src('./src/res/apps/hradi/*')
        .pipe(gulp.dest(path + '/'));
  });

};
