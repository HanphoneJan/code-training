import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';


// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...

const config: Config = {
  title: 'HanphoneJan 技术文档',
  tagline: '技术文档与知识分享',
  favicon: 'img/favicon.ico',

  // SEO 元信息
  customFields: {
    keywords: ['技术文档', '前端开发', '后端开发', '嵌入式', '机器学习', 'STM32', 'React', 'Next.js'],
  },


  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true,
  },

  // Set the production url of your site here
  url: 'https://hanphonejan.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',


  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'hanphonejan', // Usually your GitHub org/user name.
  projectName: 'HanphoneJan.github.io', // Usually your repo name.
  deploymentBranch: 'gh-pages',


  onBrokenLinks: 'throw',
  onDuplicateRoutes: 'warn',


  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'zh-CN',
    locales: ['zh-CN'],
  },


  markdown: {
    mermaid: true,
    format: 'detect',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },


  themes: [
    '@docusaurus/theme-mermaid',
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        language: ['en', 'zh'],
        searchBarPosition: 'right',
      },
    ],
  ],


  presets: [
    [
      'classic',
      {
        docs: {
          editUrl: 'https://github.com/hanphonejan/HanphoneJan.github.io/edit/main/',
          showLastUpdateTime: true,
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl: 'https://github.com/hanphonejan/HanphoneJan.github.io/edit/main/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: ["./src/css/fonts.css", "./src/css/custom.css"],
        },
      } satisfies Preset.Options,
    ],
  ],


  themeConfig: {
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'HanphoneJan',
      hideOnScroll: false,
      items: [
        {to: '/', label: '首页', position: 'left'},
        {
          type: 'docSidebar',
          sidebarId: 'defaultSidebar',
          position: 'left',
          label: '文档',
        },
        {to: '/blog', label: '博客', position: 'left'},
        {
          href: 'https://github.com/hanphonejan',
          label: 'GitHub',
          position: 'right',
          className: 'navbar-github-icon',
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.oneDark,
      additionalLanguages: ['bash', 'python', 'java', 'typescript', 'javascript', 'go', 'rust', 'sql', 'json', 'verilog'],
      magicComments: [
        {
          className: 'theme-code-block-highlighted-line',
          line: 'highlight-next-line',
          block: {start: 'highlight-start', end: 'highlight-end'},
        },
      ],
    },
    mermaid: {
      theme: {light: 'default', dark: 'dark'},
    },
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
  } satisfies Preset.ThemeConfig,
};


export default config;
