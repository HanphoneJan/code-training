import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <main className={styles.hero}>
        <div className={styles.heroContainer}>
          <h1 className={styles.title}>Code Training</h1>
          <p className={styles.subtitle}>系统化算法学习 · 长期知识积累</p>
          <div className={styles.buttons}>
            <Link href="/category/-题目库" className={styles.heroButton}>
              开始学习
            </Link>
            <Link href="/review/weekly_summary" className={styles.heroButtonSecondary}>
              学习笔记
            </Link>
          </div>
          
        </div>
      </main>
    </Layout>
  );
}
