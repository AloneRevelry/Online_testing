 $.fn.fontFlex = function(r_size) {
    var $this = this;
    $(window).resize(function() {
      var size = r_size * document.body.clientWidth/window.screen.width;
      $this.css('font-size', size + 'px');
      console.log(window.innerWidth);
    }).trigger('resize');
  };
$('#Time').fontFlex(20)
$('#Title').fontFlex(60)
$('.')


