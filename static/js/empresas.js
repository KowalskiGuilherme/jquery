$(function () {

$(".js-create-empresa").click(function () {
  var btn = $(this);  // <-- HERE
  $.ajax({
    url: btn.attr("data-url"),  // <-- AND HERE
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#modal-empresa").modal("show");
    },
    success: function (data) {
      $("#modal-empresa .modal-content").html(data.html_form);
    }
  });
});
  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-empresa").modal("show");
      },
      success: function (data) {
        $("#modal-empresa .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#empresa-table tbody").html(data.html_empresa_list);
          $("#modal-empresa").modal("hide");
        }
        else {
          $("#modal-empresa .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create empresa
  $(".js-create-empresa").click(loadForm);
  $("#modal-empresa").on("submit", ".js-empresa-create-form", saveForm);

  // Update empresa
  $("#empresa-table").on("click", ".js-update-empresa", loadForm);
  $("#modal-empresa").on("submit", ".js-empresa-update-form", saveForm);

});