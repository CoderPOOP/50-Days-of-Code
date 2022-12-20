// Link - https://exercism.org/tracks/javascript/exercises/poetry-club-door-policy/edit

// @ts-check
/**
 * Respond with the correct character, given the blurb, if this were said at
 * the front door.
 *
 * @param {string} blurb
 * @returns {string}
 */
 export function frontDoorResponse(blurb) {
    return blurb[0];
  }
  /**
   * Respond with the correct character, given the blurb, if this were said at
   * the back door.
   *
   * @param {string} blurb
   * @returns {string}
   */
  export function backDoorResponse(blurb) {
    blurb = blurb.trim();
    return blurb[blurb.length - 1];
  }
  /**
   * Capitalizes a word, meaning only the first character is a capital, and the
   * remaining letters are lower case.
   *
   * @param {string} word
   * @returns {string}
   */
  function capitalize(word) {
    return word[0].toLocaleUpperCase() + word.slice(1).toLocaleLowerCase();
  }
  /**
   * Give the password for the front-door, given the responses.
   *
   * @param {string} responses the responses
   * @returns {string} the password
   */
  export function frontDoorPassword(responses) {
    return capitalize(responses);
  }
  /**
   * Give the password for the back-door, given the responses.
   *
   * @param {string} responses the responses
   * @returns {string} the password
   */
  export function backDoorPassword(responses) {
    return capitalize(responses) + ', please';
  }