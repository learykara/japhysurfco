$(function() {
	$(".fancybox").fancybox({
		helpers: {
			arrows: 'true',
			closeBtn: 'true'
		}
	});

	var galWidth = $('.img-box').width();
	$('.img-box').css('height', galWidth + 'px');
});