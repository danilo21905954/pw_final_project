/*
 * © Bugaev Ivan
 * This code is protected by copyright.
*/

function BivBackgroundImage() {
    $('.biv-background').each(function(){
        imgUrl = $(this).data('src');
        $(this).css({'backgroundImage': 'url('+imgUrl+')'});
    });
}

BivBackgroundImage();

function BivNavBtn() {
    blockId = ".biv-left";
    classname = "active";
    if (!$(blockId).hasClass(classname)) {
        $(blockId).addClass(classname);
        $('body').addClass('noscroll');
    } else {
        $(blockId).removeClass(classname);
        $('body').removeClass('noscroll');
    }
}

function BivNavBtnSubmenu(id) {
    blockId = "#menu"+id;
    classname = "active";
    if (!$(blockId).hasClass(classname)) {
        $(blockId).addClass(classname);
    } else {
        $(blockId).removeClass(classname);
    }
}

function BivSection(id) {
    blockId = "#menu"+id;
    classname = "active";
    $(blockId).addClass(classname);
}

function BivSubSection(id,subId) {
    $("#menu"+id).addClass("active");
    $("#subMenu"+subId).addClass("active");
}

function BivPanelAlignment() {
    $('.biv-panel').css({'height': ''});
    windowHeight = $(window).height();
    blockHeight = $('.biv-panel').height();
    if( windowHeight > blockHeight ) {
        $('.biv-panel').css({'height': windowHeight+'px'});
    }
}

BivPanelAlignment();

$(function() {
  $(window).resize(function() {
    BivPanelAlignment();
  });
});

var bivSpoilerId = 1;
var bivSpoilerStart = 0;

function BivSpoiler(id) {
    if( bivSpoilerStart == '1' ) {
        $("#bivFormSpoilerBtn"+bivSpoilerId).removeClass("active");
        $("#bivFormSpoilerList"+bivSpoilerId).removeClass("active");
    }
    if( bivSpoilerStart == '0' ) {
        bivSpoilerStart = 1;
    }
    $("#bivFormSpoilerBtn"+id).addClass("active");
    $("#bivFormSpoilerList"+id).addClass("active");
    bivSpoilerId = id;
}

BivSpoiler(bivSpoilerId);

