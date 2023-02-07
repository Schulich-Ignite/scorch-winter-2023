# Filesaverjs

You can also save files from the browser, with a few caveats:

1. You can only save to /Downloads

2. You can only use certain file types



To do this there are 3 steps:

1. import [FileSaver](https://github.com/eligrey/FileSaver.js/) (from CDN ideally)

2. Create a string with your content

3. Create a [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) (a file-like object)

4. Export the Blob to a file with FileSaver

```js
blob = new Blob([html), {type:"text/html;charset=utf-8"});
saveAs(blob, "Hello World.html");
```


