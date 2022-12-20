// Link - https://exercism.org/tracks/javascript/exercises/word-count/edit

//
// This is only a SKELETON file for the 'Word Count' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
export const countWords = (sentence) => {
    //throw new Error('Remove this statement and implement this function');
    let arr = sentence.match(/\w+(?:'\w+)*/g);
    let unique = [...new Set(arr)];
    let obj = new Object;
    unique.forEach(elem => obj[elem.toLowerCase()] = 0);
    arr.forEach(elem => obj[elem.toLowerCase()]++);  
    return obj;
  };  