# Filtering!

This library is designed to help you filter HTML elements based on categories. It features:

- A non-intrusive opt-in class-based filtering system to not break existing functionality
- Reconfigurabile class keywords for better semantic class definitions

## Usage

Below are details of how to use filtering!

### Installing

To use filtering! import the main js file (`filtering.js`) and the main CSS file (`filtering.css`) in the page you want to use it on.

### How it works

filtering! will add one of two classes to elements based on the filters selectd, and if the element has the correct filter. Any elements with the show class will be displayed, andy elements with the hide class will be hidden. 

### Reconfiguring keywords

By default filtering! uses animal as it's keyword. To change this replace all instances of animal in the javascript, html and CSS.

### Setting filters

To create a filter you will need to add a new span element, with a class of filter, and a data-filter attribute with the filter word. 

*Keep in mind "all" is a reserved filter to display all items*

For example:

```html
<div class="filters">
    <span class="filter" data-filter="all">ALL</span>
    <span class="filter" data-filter="reptile">REPTILE</span>
    <span class="filter" data-filter="mammal">Mammal</span>
</div>
```

Would provide 3 clickable filters, one for all elements, one for those with data-filter set to either reptile or animal.

### Assigning filters to elements

Once you have created your filters you need to setup elements to be filtered. 

To do this you need to use the **plural form** of your keyword (so animals if your keyword is animal) for the container that will hold all your other elements that you want to filter (which will use the **singular**). 

For example:

```html
<div class="animals">
  <div class="animal" data-filter="reptile">
    Komodo Dragon
  </div>
  <div class="animal" data-filter="mammal">
    Fox
  </div>
</div>
```

This can be combined with the filter examples above so that only the Komodo Dragon would show up if people clicked the REPTILE filter, and Fox if they clicked MAMMAL.

### Modifying CSS animation

The way the filtering system actually works is that there are two classes, show and hide. These classes have CSS animations that fade the elements in and out. If you want to mess with these timings you can find them in the first 35 lines of the CSS, **DO NOT REMOVE THESE**, or it will break!

---

## Hints

You can find hints in the readme if you get stuck!