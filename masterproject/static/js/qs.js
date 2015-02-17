var qs = qs || {};
qs.bindForm = function(bindings, id) {
  
  var createHandler = function(key, value) {
    $("#"+key).click(function() { // klikker på bilde
      $("#" + id).val(value);

      var src = $(this).attr('src');
      var src_selected = src.replace('.svg', '-selected.svg');

      //fjerner alle klasser og setter src til svart ikon
      $("#content-module").find('img').removeClass('selected');

      //Legger til klassen selected på bildet som ble klikket på
      $(this).addClass('selected');

      //Endrer valgt bilde til grønt
      $(this).attr("src",src_selected);

      //Fader ut skjermen
      $( "#wrapper").fadeOut( "slow", function() {
        $("#btn-post").click();
      });
    });
  };
  for (key in bindings) {
    createHandler(key, bindings[key]);
  }
};

function addNationality() {
  $('.dropdown').dropdown({
    onChange: function(val) {
      $('#id_nationality').val(val);
    },
    onShow: function() {
      $('#navigation').hide();
    },
    onHide: function() {
      $('#content-module').click();
      $('#navigation').show();
    },
  });
  $('#submit_nationality').click(function() {
    $('#btn-post').click();
  });
}

function addPattern() {
  var radius = 0.6*(screen.width/8);
  var margin = 0.2*(screen.width/4);

  console.log(radius);
  console.log(margin);

  var lock = new PatternLock('#patternContainer', {
    onDraw:function(pattern){
      pattern = lock.getPattern();
      if(pattern.length>=4){
        $('#retrypattern').click(function() {
          lock.reset();
        });
        $('#continue').click(function() {
          $('#id_sequence').val(pattern);
          $( "#wrapper").fadeOut( "slow", function() {
            $('#btn-post-continue').click();
          });
        });
        $('#retry').click(function() {
          $('#id_sequence').val(pattern);
          $('#btn-post-retry').click();
        });
      }
      else{
        lock.error();
        $('#retrypattern').click(function() {
          lock.reset();
        });
      }
    },
    radius: radius,
    margin: margin,
  });
};

//AndroidOS, BlackBerryOS, PalmOS, SymbianOS, WindowsMobileOS, WindowsPhoneOS, iOS, MeeGoOS, MaemoOS, JavaOS, webOS, badaOS, BREWOS
function getMobileOperatingSystem() {
    var md = new MobileDetect(window.navigator.userAgent);
    var os = md.os();
    $('#os_notfound').hide();
    $('#os_found').show();

    if(os==null){
      $('#os_notfound').show();
      $('#os_found').hide();
      $('.dropdown').dropdown({
        onChange: function(val) {
          $('#id_mobileOS').val(val);  
        }
      });
      $('#submitOS').click(function() {
        $('#btn-post').click();
      });
    }
    else if(os.match("iOS")) {
      $('img#yes').attr('id', 'ios');
      $('img#no').attr('id', 'no_ios');
      $('img#unknown').attr('id', 'unknown_ios');
      $('img#mobileOS').attr('src', '/static/images/icons/ios.svg');
      $('label#mobile-label').text('iOS (iPhone)');
    }
    else if(os.match("Android")) {
      $('img#yes').attr('id', 'android');
      $('img#no').attr('id', 'no_android');
      $('img#unknown').attr('id', 'unknown_android');
      $('img#mobileOS').attr('src', '/static/images/icons/android.svg');
      $('label#mobile-label').text('Android');
    }
    else if(os.match("BlackBerry")) {
      $('img#yes').attr('id', 'blackberry');
      $('img#no').attr('id', 'no_blackberry');
      $('img#unknown').attr('id', 'unknown_blackberry');
      $('img#mobileOS').attr('src', '/static/images/icons/blackberry.svg');
      $('label#mobile-label').text('BlackBerry');
    }
    else if(os.match("Windows")){
      $('img#yes').attr('id', 'windows');
      $('img#no').attr('id', 'no_windows');
      $('img#unknown').attr('id', 'unknown_windows');
      $('img#mobileOS').attr('src', '/static/images/icons/windows.svg');
      $('label#mobile-label').text('Windows');
    }
    else {
      $('#os_notfound').show();
      $('#os_found').hide();
      $('.dropdown').dropdown({
        onChange: function(val) {
          $('#id_mobileOS').val(val);  
        }
      });
      $('#submitOS').click(function() {
        $('#btn-post').click();
      });
    }
};

function addAge() {
    $('#submitAge').click(function() {
      $("#id_age").val($("#age").val());
      $('#btn-post').click();
    });
};

function setScreenSize() {
  $('#id_actual_screenheight').val(screen.width);
  $('#id_actual_screenwidth').val(screen.height);
  // $(window).width()
};

function fixedFooter() {
  $("#age").focus(function(){
    $('#navigation').hide();
  });
  $("#age").blur(function(){
    $('#navigation').show();
  });
};

