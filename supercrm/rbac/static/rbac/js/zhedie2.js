    $('.parent').click(function () {

        // fa-caret-right"
        $(this).find('.icon').toggleClass('fa-caret-right');
        $(this).nextUntil('.parent').toggleClass('hidden');

    });




