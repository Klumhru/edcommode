module.exports = function(gulp) {

  gulp.task('icons', function() {
    var gutil = gulp.plugin.util,
        prod  = gutil.env.prod;

    return gulp.src('./src/style/icons/**/*.{png,ico,xml}')
      .pipe( gulp.plugin.plumber() )

      .pipe( gulp.dest(prod ? './dist/style/icons/' : './dev/style/icons/') )
      .pipe( prod ? gutil.noop() : gulp.plugin.connect.reload() );
  });

};
