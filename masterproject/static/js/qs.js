var qs = qs || {};
qs.bindForm = function(bindings, id) {
  
  var createHandler = function(key, value) {
    $("#"+key).click(function() { // klikker på bilde
      $("#" + id).val(value);
      $("div#content").find('img').removeClass('selected');
      $(this).addClass('selected');
    });
  };
  for (key in bindings) {
    createHandler(key, bindings[key]);
  }

};

var populateNations = function(divId) {
      $select = $("#" + divId);
      
      for (var i = 0; i < nations.length; ++i) {
        $select.append($("<option></option>")
          .attr("value",nations[i].code)
          .text(nations[i].name)); 
      }
    };


