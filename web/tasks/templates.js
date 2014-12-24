
module.exports = function(gulp) {

  gulp.task('templates', function() {
    var gutil = gulp.plugin.util,
        prod  = gutil.env.prod,
        data = {
          'env': prod ? 'production' : 'development',
          'flags': gutil.env
        };

    return gulp.src(['./src/apps/**/*.jade'])
      .pipe( gulp.plugin.plumber() )
      .pipe( gulp.plugin.jade({pretty: true, data: data}))
      .on('error', gulp.plugin.notify.onError(function(error){
        return error.message;
      }))
      .pipe( gulp.dest(prod ? './dist/' : './dev/') )
      .pipe( prod ? gutil.noop() : gulp.plugin.connect.reload() );
  });
};
