function tipCalculator(quality, bill) {
  if (quality === 'bad') {
    return bill * 0.05;
  } else if (quality === 'ok') {
    return bill * 0.15;
  } else if (quality === 'good') {
    return bill * 0.2;
  } else if (quality === 'excellent') {
    return bill * 0.3;
  } else {
    return bill * 0.18;
  }
}
