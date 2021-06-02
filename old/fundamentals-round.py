# Return the first longest string consisting of k consecutive strings taken in the array

function findNb(m) {
    for (i=1;m>0;m-=(i++)**3);
    return (m == 0) ? i-1 : (-1);
}

