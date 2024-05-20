function uncheck_other_years(checkbox) {
    var yearCheckboxes = document.querySelectorAll('input[name^="is_"]');
    yearCheckboxes.forEach(function(checkboxElement) {
        if (checkboxElement !== checkbox && checkboxElement.checked) {
            checkboxElement.checked = false;
        }
    });
}
