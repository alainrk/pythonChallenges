// Create three functions that one needs to be able to call upon an array
// All: This function returns true only if the predicate supplied returns true for all the items in the array
// None: This function returns true only if the predicate supplied returns false for all the items in the array
// Any: This function returns true if at least one of the items in the array returns true for the predicate supplied

Array.prototype.all = function (p) {
  for (i = 0; i < this.length; i++)
    if (!p(this[i])) return false;
  return true;
};

Array.prototype.none = function (p) {
  for (i = 0; i < this.length; i++)
    if (p(this[i])) return false;
  return true;
};

Array.prototype.any = function (p) {
  for (i = 0; i < this.length; i++)
    if (p(this[i])) return true;
  return false;
};
