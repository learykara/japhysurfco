$(function() {
	$(".fancybox").fancybox({
		helpers: {
			arrows: 'true',
			closeBtn: 'true'
		}
	});

	var galWidth = $('.img-box').width();
	$('.img-box').css('height', galWidth + 'px');

	if (window.innerWidth <= 800) {
		$('#gallery').removeClass('mCustomScrollbar');
		$('#products').removeClass('mCustomScrollbar');
	}
});