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
            <Link href="/docs/intro" className={styles.heroButton}>
              开始学习
            </Link>
            <Link href="/review/weekly_summary" className={styles.heroButtonSecondary}>
              学习笔记
            </Link>
          </div>
          
          <div style={{marginTop: '3rem', textAlign: 'center'}}>
            <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.5rem', maxWidth: '900px', margin: '0 auto'}}>
              <div style={{padding: '1.5rem', borderRadius: '8px', background: 'var(--ifm-background-surface-color)', border: '1px solid var(--ifm-color-emphasis-200)'}}>
                <h3>📚 题目库</h3>
                <p>原子化存储，每题独立</p>
              </div>
              <div style={{padding: '1.5rem', borderRadius: '8px', background: 'var(--ifm-background-surface-color)', border: '1px solid var(--ifm-color-emphasis-200)'}}>
                <h3>🎯 知识点</h3>
                <p>系统化整理，体系清晰</p>
              </div>
              <div style={{padding: '1.5rem', borderRadius: '8px', background: 'var(--ifm-background-surface-color)', border: '1px solid var(--ifm-color-emphasis-200)'}}>
                <h3>🔧 模板库</h3>
                <p>常用代码，开箱即用</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
