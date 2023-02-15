`Better Buy` is an innovative ecommerce store that focuses on selling electronics that are either open box or unopened. The store provides customers with an extensive selection of electronics ranging from smartphones, laptops, gaming consoles, and many other gadgets at an affordable price. Better Buy offers its customers the opportunity to purchase high-quality products at a fraction of the retail price, making it a go-to destination for tech-savvy shoppers looking to save on their purchases.

The store's online platform offers a user-friendly interface that simplifies the purchasing process. Customers can browse the store's offerings, and purchase products with ease. Better Buy is dedicated to providing customers with excellent customer service and ensuring that they have a smooth and satisfactory shopping experience. With its focus on affordability, quality, and convenience, Better Buy is poised to become a major player in the electronics ecommerce market.

## Deliverables

To get full points you have to complete all of the levels. They build on top of each other as you go.

For all 3 levels use the code in `starter.py` to start. There is also a template started for you it uses `base.jinja` as the template to inherit from, and has some components in `/components` you can use.

### Level 1

Build a products page that shows off products:

- Create a new component called `/components/product-card.jinja`
    - Make it a card that shows off:
        - A product image
        - Product name
        - Product price
        - Product description
- Bring in the product data to `products.jinja` so it can be used
- Update `products.jinja` so it uses the product information, and your new component to show off the products (any layout is fine (3 column, 4 column etc.))

### Level 2

Create a product page:

- Create a template called `product.jinja`, this will take in an individual product and showoff the product image, name, price and description. If a product has `sale` set to true, then show the original in red (or a strikethrough [`.text-decoration-line-through`] ), and a %10 lower price, i.e. $̶2̶9̶9̶.̶9̶9̶  $269.99 (or $299.99 in red)
- You should override the title block, and main block
- Update the export function so 1 page per product is exported (i.e. a product called phone should export to `phone.html` using the `product.jinja` file)

### Level 3

Create a shopping cart:

- update `product.jinja` to use the javascript function `addToCart()` 
  - Defined in `cart.js`, but imported in `base.jinja` so it's available everywhere
- In `checkout.jinja` write javascript that updates the cart with (get the information with `getCart()`):
  - The correct number of items in the cart (`#cart-items-indicator`)
  - The prices of each item (`#cart-list`)
  - The amount saved because of the sale (`#cart-list`)

*You **do not** need to implement any of the actual checkout logic (payment etc.), this is just there for appearance!*

## Hints

- Some updates will require updating the template, some will require updating the python code
- A tip for styling images that are different aspect ratios is to set `object-fit:cover` for an `img` tag. This means zoom the image in to the size I want details [here](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
- The data for the products can be found in `products.py`, look at how the profile page loads it's data for help on how to load data in specific pages
- To re-use `product.jinja` for every product, you will need to update the `export_all_pages()` function so that it runs with each product, and exports each product
- if you misname a variable in a partial **an error will not be thrown**. For example if you say `name` instead of `product.name` there will be **no error** it will just be blank
- If you are lazy you can use [this template](https://startbootstrap.com/template/shop-homepage) or [this template](https://startbootstrap.com/template/shop-item) to make building faster


