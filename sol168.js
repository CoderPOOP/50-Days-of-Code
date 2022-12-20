// Link - https://exercism.org/tracks/javascript/exercises/gigasecond

const gigasecondToMillisecond = 10e11;

export const gigasecond = date =>
  new Date(date.getTime() + gigasecondToMillisecond);