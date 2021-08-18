<script>
$(function()
  {
  $(".lp-button.button.button-complete-item.button-complete-lesson.lp-btn-complete-item").attr("disabled", "disabled");
  setTimeout(function()
             {
    $(".lp-button.button.button-complete-item.button-complete-lesson.lp-btn-complete-item").removeAttr("disabled");
  },10000)
})
</script>
