(function($) {
    $(document).ready(function() {
        // Find the import CSV button
        var importCsvButton = $('a[href*="import-csv/"]');
        if (importCsvButton.length) {
            // When the button is clicked, trigger the file input dialog
            importCsvButton.on('click', function(event) {
                event.preventDefault();
                $('input[type="file"]').click();
            });
        }
    });
})(django.jQuery);
