#!/usr/bin/env node

import Parser from 'rss-parser';
import pc from 'picocolors';
import minimist from 'minimist';
import { HttpsProxyAgent } from 'https-proxy-agent';

// Define help/usage instruction
const usage = `
${pc.bold(pc.cyan('Google News CLI Tool'))}
Usage:
  ${pc.green('google-news')} [options]

Options:
  ${pc.yellow('-s, --search <query>')}  Search for specific news topics
  ${pc.yellow('-t, --topic <topic>')}    Get news for a specific topic
                         Topics: ${pc.dim('world, nation, business, technology, entertainment, sports, science, health')}
  ${pc.yellow('-l, --limit <number>')}   Number of news items to display (default: 10)
  ${pc.yellow('-h, --help')}             Display this help message

Examples:
  ${pc.green('google-news --topic technology')}
  ${pc.green('google-news --search "artificial intelligence" --limit 5')}
`;

const TOPICS = {
  world: 'WORLD',
  nation: 'NATION',
  business: 'BUSINESS',
  technology: 'TECHNOLOGY',
  entertainment: 'ENTERTAINMENT',
  sports: 'SPORTS',
  science: 'SCIENCE',
  health: 'HEALTH'
};

async function main() {
  const argv = minimist(process.argv.slice(2), {
    string: ['search', 'topic', 'limit'],
    boolean: ['help'],
    alias: {
      s: 'search',
      t: 'topic',
      l: 'limit',
      h: 'help'
    }
  });

  if (argv.help) {
    console.log(usage);
    process.exit(0);
  }

  const limit = parseInt(argv.limit, 10) || 10;
  let url = 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en';
  let titleHeader = 'Top Stories';

  if (argv.search) {
    const query = argv.search;
    url = `https://news.google.com/rss/search?q=${encodeURIComponent(query)}&hl=en-US&gl=US&ceid=US:en`;
    titleHeader = `Search: "${query}"`;
  } else if (argv.topic) {
    const topicKey = argv.topic.toLowerCase();
    const googleTopic = TOPICS[topicKey];
    if (!googleTopic) {
      console.error(pc.red(`Error: Invalid topic "${argv.topic}".`));
      console.log(`Available topics: ${pc.dim(Object.keys(TOPICS).join(', '))}`);
      process.exit(1);
    }
    url = `https://news.google.com/news/rss/headlines/section/topic/${googleTopic}?hl=en-US&gl=US&ceid=US:en`;
    titleHeader = `Topic: ${argv.topic.toUpperCase()}`;
  }

  console.log(pc.cyan(`\nFetching news from Google News [${titleHeader}]...\n`));

  // Handle environment proxies
  const proxyUrl = process.env.https_proxy || process.env.http_proxy || process.env.HTTPS_PROXY || process.env.HTTP_PROXY;
  const parserOption = {};
  if (proxyUrl) {
    parserOption.requestOptions = {
      agent: new HttpsProxyAgent(proxyUrl)
    };
  }

  const parser = new Parser(parserOption);
  try {
    const feed = await parser.parseURL(url);
    const items = feed.items.slice(0, limit);

    if (items.length === 0) {
      console.log(pc.yellow('No news items found.'));
      return;
    }

    items.forEach((item, index) => {
      // Clean title and extract source if possible (usually formatted as "Title - Source")
      const title = item.title || '';
      const parts = title.split(' - ');
      const source = parts.length > 1 ? parts.pop() : 'Google News';
      const cleanTitle = parts.join(' - ');

      const pubDate = item.pubDate ? new Date(item.pubDate).toLocaleString() : 'Unknown date';

      console.log(`${pc.bold(pc.green(`${index + 1}.`))} ${pc.bold(cleanTitle)}`);
      console.log(`   ${pc.dim('Source:')} ${pc.magenta(source)} | ${pc.dim('Published:')} ${pc.yellow(pubDate)}`);
      console.log(`   ${pc.dim('Link:')} ${pc.blue(pc.underline(item.link))}`);
      console.log();
    });
  } catch (error) {
    console.error(pc.red('Error fetching or parsing the RSS feed:'), error.message);
    process.exit(1);
  }
}

main();
