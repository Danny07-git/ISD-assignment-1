document.addEventListener("DOMContentLoaded", function() {
    // Adds the bootstrap css classes to table elements in the document
    document.querySelectorAll("table").forEach(function(table) {
      table.classList.add("table");
      table.classList.add("table-responsive-sm");
      table.classList.add("table-bordered");
      table.classList.add("table-striped");
    });

    // Hides the table of contents elements when using the
    // mkdocs-include-markdown-plugin
    $('.toc').each(function(index) {
      if(index === 0)
        return;
      $(this).css({"display":"none"});
    });
});