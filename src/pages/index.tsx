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
          <h1 className={styles.title}>算法训练知识库</h1>
          <p className={styles.subtitle}>题目库、知识点、模式与模板的系统化整理</p>
          <div className={styles.buttons}>
            <Link href="/category/-题目库" className={styles.heroButton}>
              进入题目库
            </Link>
            <Link href="/category/-复习系统" className={styles.heroButtonSecondary}>
              复习总结
            </Link>
          </div>
          
        </div>
      </main>
    </Layout>
  );
}
