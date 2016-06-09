// Create a function christmasTree(height) that returns a christmas tree of the correct height
//
// christmasTree(5) should return:
//
//     *
//    ***
//   *****
//  *******
// *********
// Height passed is always an integer between 0 and 100.
//
// Use \n for newlines between each line.
//
// Pad with spaces so each line is the same length. The last line having only stars, no spaces.

function star(n,s){
  r="";
  for (var i=0;i<n;i++) r+=s;
  return r;
}

function christmasTree(height) {
  tree="";
  for (var i=height;i>0;i--)
    tree = star(height-i," ") + star(i*2-1,"*") + star(height-i," ") + ((i!=height) ? "\n" : "") + tree;
  return tree;
}
