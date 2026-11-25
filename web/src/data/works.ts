// Projects data. Sections → click an item to open its detail page.
// 纯数据驱动：增删板块 / 作品只改本文件，Works.jsx 仅负责渲染。
//
// 板块字段：
//   id        唯一标识（用于 framer layoutId 共享元素动画）
//   no        编号 '01'…'05'
//   title     板块标题
//   tagline   索引行右侧一句话
//   items[]   扁平作品列表：{ name, meta?, tags?, link? }
//             点击 item 弹出全屏详情，可补充可选媒体/文案字段：
//             { image?, video?, year?, desc? }（缺省时媒体用占位、简介回退 meta/标签）
//   groups[]  分组作品（与 items 二选一）：{ heading, items: string[] }
//   awards[]  奖项 chip（可选）
//   footer    底部技术/备注一行（可选）

export interface WorkListItem {
  name: string
  meta?: string
  tags?: string[]
  link?: string
  slug?: string
}

export interface WorkGroup {
  heading: string
  items: string[]
}

export interface WorkSection {
  id: string
  no: string
  title: string
  tagline: string
  items?: WorkListItem[]
  groups?: WorkGroup[]
  awards?: string[]
  footer?: string
}

export interface WorksLang {
  title: string
  closeLabel: string
  openLabel: string
  hint: string
  awardsLabel: string
  visitLabel: string
  detailPlaceholder: string
  phImageLabel: string
  phButtonLabel: string
  countLabel: (n: number) => string
  sections: WorkSection[]
}

export const WORKS: Record<'en', WorksLang> = {
  en: {
    title: 'Projects',
    closeLabel: 'Back',
    openLabel: 'Explore',
    hint: 'Keep scrolling',
    awardsLabel: 'Awards',
    visitLabel: 'View project',
    detailPlaceholder: 'Project write-up coming soon.',
    phImageLabel: 'Image / Video',
    phButtonLabel: 'Link',
    countLabel: (n) => `${n} projects`,
    // TODO(Talha): replace every [bracketed] value with your real projects.
    // Add a write-up for a project by creating src/content/works/<slug>.md (see example.md).
    sections: [
      {
        id: 'research',
        no: '01',
        title: 'Research',
        tagline: '[Your lab / thesis topic]',
        items: [
          { name: '[Thesis title]', meta: '[Year]', tags: ['[Method]', '[Tool]'], slug: 'thesis' },
          { name: '[Paper or poster]', meta: '[Venue]', slug: 'paper' },
        ],
      },
      {
        id: 'projects',
        no: '02',
        title: 'Projects',
        tagline: '[What you build]',
        items: [
          { name: '[Project one]', meta: '[One-line summary]', slug: 'project-one' },
          { name: '[Project two]', meta: '[One-line summary]', slug: 'project-two' },
          { name: '[Project three]', meta: '[One-line summary]', slug: 'project-three' },
        ],
        footer: '[Tools: Python · Blender · …]',
      },
      {
        id: 'experience',
        no: '03',
        title: 'Teaching & Work',
        tagline: '[TA / RA / internships]',
        items: [{ name: '[Role at place]', meta: '[Dates]', slug: 'experience-one' }],
      },
    ],
  },
}

// 板块配图（横向画廊每张卡片左侧的整高封面）。放到 public/works/covers/ 下。
// 缺图时左栏用大编号渐变占位，放入图片后自动点亮。
export const SECTION_COVERS: Record<string, string> = {
  // e.g. research: `${import.meta.env.BASE_URL}works/covers/research.jpg`,
}

// 统计一个板块的作品数（items 或 groups 求和），用于索引行 hover 显示
export function sectionCount(section: WorkSection): number {
  if (section.items) return section.items.length
  if (section.groups) return section.groups.reduce((n, g) => n + g.items.length, 0)
  return 0
}
