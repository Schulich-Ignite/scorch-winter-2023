/* Heavily Modified from https://codepen.io/vskand/pen/MWKKKYK */

// Find elements with filter class
const filters = document.querySelectorAll('.filter');

filters.forEach(filter => { 

    // Add listener for when you click something
    filter.addEventListener('click', function() {

    // Find out which filter has been clicked
    let selectedFilter = filter.getAttribute('data-filter');

    let items = Array.from(document.getElementsByClassName("post"));
    let itemsToShow = Array.from(document.querySelectorAll(`.posts [data-filter='${selectedFilter}']`));

    let itemsToHide = items.filter(x => !itemsToShow.includes(x));

    if (selectedFilter == 'all') {
        itemsToHide = [];
        // Find elements that have ANY data-filter set
        itemsToShow = document.querySelectorAll('.posts [data-filter]');
    }

    itemsToHide.forEach(el => {
        el.classList.add('hide');
        el.classList.remove('show');
    });

    itemsToShow.forEach(el => {
        el.classList.remove('hide');
        el.classList.add('show'); 
    });

    });
});