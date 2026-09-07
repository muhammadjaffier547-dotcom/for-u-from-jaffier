// Drop Dead - Olivia Rodrigo (TikTok Aesthetic Terminal Lyrics)
// Run with: node drop_dead.js

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const Colors = {
  reset: "\x1b[0m",
  bold: "\x1b[1m",
  dim: "\x1b[2m",
  pink: "\x1b[38;2;255;105;180m",
  purple: "\x1b[38;2;186;85;211m",
  cyan: "\x1b[38;2;0;255;255m",
  blue: "\x1b[38;2;100;149;237m",
  yellow: "\x1b[38;2;255;215;0m",
  gray: "\x1b[38;2;128;128;128m",
};

const lyrics = [
  { text: "Oh, one night I was bored in bed", charDelay: 75, pause: 450, color: Colors.pink },
  { text: "And stalked you on the internet", charDelay: 70, pause: 550, color: Colors.pink },
  { text: "It's feminine intuition", charDelay: 80, pause: 600, color: Colors.cyan },
  { text: "'Cause I always had a vision of us standing like this", charDelay: 55, pause: 700, color: Colors.purple },
  { text: "All pressed up in the bathroom line", charDelay: 70, pause: 500, color: Colors.blue },
  { text: "You're lookin' like an angel on the walls of Versailles", charDelay: 58, pause: 650, color: Colors.yellow },
  { text: "The most alive I've ever been", charDelay: 75, pause: 850, color: Colors.cyan },
  { text: "But kiss me and I might...", charDelay: 90, pause: 600, color: Colors.pink },
  { text: "...DROP DEAD 🖤✨", charDelay: 110, pause: 2000, color: Colors.pink + Colors.bold },
];

async function typeWriter(text, delay, color) {
  process.stdout.write(color);
  for (const char of text) {
    process.stdout.write(char);
    await sleep(delay);
  }
  process.stdout.write(Colors.reset + "\n");
}

async function start() {
  console.clear();
  console.log(`${Colors.purple}${Colors.bold}┌────────────────────────────────────────────────────┐${Colors.reset}`);
  console.log(`${Colors.purple}${Colors.bold}│      🎧 Now Playing: Olivia Rodrigo - Drop Dead     │${Colors.reset}`);
  console.log(`${Colors.purple}${Colors.bold}└────────────────────────────────────────────────────┘${Colors.reset}\n`);

  await sleep(1000);

  for (const item of lyrics) {
    await typeWriter(item.text, item.charDelay, item.color);
    await sleep(item.pause);
  }

  console.log(`\n${Colors.gray}─── [Playback Finished] ───${Colors.reset}\n`);
}

start();

