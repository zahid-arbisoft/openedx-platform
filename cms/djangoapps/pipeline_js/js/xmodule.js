// Updated MathJax CDN reference to version 2.7.9
var mathJaxScript = document.createElement('script');
mathJaxScript.src = 'https://cdn.jsdelivr.net/npm/mathjax@2.7.9/MathJax.js?config=TeX-AMS_HTML';
mathJaxScript.onload = function() {
  console.log('MathJax script loaded successfully');
  // Initialize MathJax here if needed
};
mathJaxScript.onerror = function() {
  console.error('Failed to load MathJax script');
};
document.head.appendChild(mathJaxScript);

// Test function to ensure MathJax is initialized correctly
function testMathJaxInitialization() {
  if (typeof MathJax !== 'undefined' && MathJax.Hub) {
    console.log('MathJax is initialized correctly');
  } else {
    console.error('MathJax is not initialized correctly');
  }
}

testMathJaxInitialization();