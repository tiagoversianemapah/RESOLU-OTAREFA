const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
require('mathjax-full/js/input/tex/AllPackages.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const html = mathjax.document(fs.readFileSync(process.argv[2], 'utf8'), {
  InputJax: new TeX({inlineMath: [['$', '$']], packages: ['base','ams','newcommand','noundefined','boldsymbol']}),
  OutputJax: new SVG({fontCache: 'global'})
});
html.render();
fs.writeFileSync(process.argv[3], adaptor.doctype(html.document) + adaptor.outerHTML(adaptor.root(html.document)));
