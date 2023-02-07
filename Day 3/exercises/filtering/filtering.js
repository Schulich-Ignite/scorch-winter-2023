/* Heavily Modified from https://codepen.io/vskand/pen/MWKKKYK */

// Find elements with filter class
const filters = document.querySelectorAll('.filter');

const keyword = "post" // The keyword to use to select

filters.forEach(filter => { 

    // Add listener for when you click something
    filter.addEventListener('click', function() {

    // Find out which filter has been clicked
    let selectedFilter = filter.getAttribute('data-filter');

    // Get all items and the list of item to show
    let items = Array.from(document.getElementsByClassName(keyword));
    let itemsToShow = Array.from(document.querySelectorAll(`.${keyword}s [data-filter='${selectedFilter}']`));

    // Determine items to hide as the set difference of the items and the items to show
    let itemsToHide = items.filter(x => !itemsToShow.includes(x));

    // Allow for all filter
    if (selectedFilter == 'all') {
        itemsToHide = [];
        // Find elements that have ANY data-filter set
        itemsToShow = document.querySelectorAll(`.${keyword}s > *`);
    }

    // Hide items that should be hidden
    itemsToHide.forEach(el => {
        el.classList.add('hide'); // add hide class
        el.classList.remove('show'); // remove show class
    });

    // Show items that should be shown
    itemsToShow.forEach(el => {
        el.classList.remove('hide'); // remove hide class
        el.classList.add('show');  // add show class
    });

    });
});