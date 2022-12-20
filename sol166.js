// Link - https://exercism.org/tracks/javascript/exercises/elyses-enchantments/edit

// @ts-check
/**
 * Retrieve card from cards array at the 0-based position
 *
 * @param {number[]} cards
 * @param {number} position
 *
 * @returns {number} the card
 */
 export function getItem(cards, position) {
    return cards[position];
    throw new Error('Implement the getItem function');
  }
  /**
   * Exchange card with replacementCard at the 0-based position
   *
   * @param {number[]} cards
   * @param {number} position
   * @param {number} replacementCard
   *
   * @returns {number[]} the cards with the change applied
   */
  export function setItem(cards, position, replacementCard) {
    cards[position] = replacementCard;
    return cards;
    throw new Error('Implement the setItem function');
  }
  /**
   * Insert newCard at the end of the cards array
   *
   * @param {number[]} cards
   * @param {number} newCard
   *
   * @returns {number[]} the cards with the newCard applied
   */
  export function insertItemAtTop(cards, newCard) {
    cards.push(newCard);
    return cards;
    throw new Error('Implement the insertItemAtTop function');
  }
  /**
   * Remove the card at the 0-based position
   *
   * @param {number[]} cards
   * @param {number} position
   *
   * @returns {number[]} the cards without the removed card
   */
  export function removeItem(cards, position) {
    cards.splice(position, 1);
    return cards;
    throw new Error('Implement the removeItem function');
  }
  /**
   * Remove card from the end of the cards array
   *
   * @param {number[]} cards
   *
   * @returns {number[]} the cards without the removed card
   */
  export function removeItemFromTop(cards) {
    cards.pop();
    return cards;
    throw new Error('Implement the removeItemFromTop function');
  }
  /**
   * Insert newCard at beginning of the cards array
   *
   * @param {number[]} cards
   * @param {number} newCard
   *
   * @returns {number[]} the cards including the new card
   */
  export function insertItemAtBottom(cards, newCard) {
    cards.unshift(newCard);
    return cards;
    throw new Error('Implement the insertItemAtBottom function');
  }
  /**
   * Remove card from the beginning of the cards
   *
   * @param {number[]} cards
   *
   * @returns {number[]} the cards without the removed card
   */
  export function removeItemAtBottom(cards) {
    cards.shift();
    return cards;
    throw new Error('Implement the removeItemAtBottom function');
  }
  /**
   * Compare the number of cards with the given stackSize
   *
   * @param {number[]} cards
   * @param {number} stackSize
   *
   * @returns {boolean} true if there are exactly stackSize number of cards, false otherwise
   */
  export function checkSizeOfStack(cards, stackSize) {
    const size = cards.length;
    return size === stackSize;
    throw new Error('Implement the checkSizeOfStack function');
  }