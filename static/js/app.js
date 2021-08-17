
// display or hide input field on click on +
$('.fa-plus').on('click', function(){
  $('input').slideToggle();
})


// change css style on click on a to do
$('ul').on('click', 'li', function(){
  $(this).toggleClass('done');
})


// add tex on keypress in input
$('input').on('keypress', function(e){
  if (e.which === 13) {
      value = $('input').val();
      $.ajax({
          type: "POST",
          url: "/todo",
          data: JSON.stringify({todo:value}),
          dataType: "json",
          contentType : "application/json",
          success: function(result) {
            location.reload();
          }
      });
  }
})

// delete to do
$('ul').on('click','span', function(e){
    e.stopPropagation();
    id = $(this).attr("val");
    parent = $(this).parent();
    $.ajax({
          type: "DELETE",
          url: "/todo?id=" + id,
          success: function(result) {
            parent.fadeOut();
            console.log("success");
          }
      });
})
