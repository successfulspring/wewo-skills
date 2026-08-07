# `wewo-prd` Skill 需求说明

## 1. Skill 定位

`/wewo-prd` 是 `wewo-skills` 中负责需求澄清和 PRD 生成的 Skill。

它面向真实软件开发场景中不完整、模糊或缺少上下文的原始需求。用户提供的内容可能只是：

- 一句话；
- 一段文字；
- 一张图片；
- 一个 TXT 文件；
- 一个 Word、Excel、PPT、PDF 等 Office 文件；
- 多份相互关联的需求材料；
- 当前对话中描述的一个初步想法。

Skill 不应直接根据这些原始材料生成 PRD，而应先理解已有信息，再通过多轮追问帮助用户逐步明确需求，最终生成可作为后续设计和开发依据的 `01-prd.md`。

------

## 2. 核心目标

`/wewo-prd` 需要完成两个连续步骤：

### 第一阶段：需求澄清

参考 Matt Pocock 的 `grill-me` 思路，将模糊需求拆解成一系列需要确认的产品决策，通过递进式追问帮助用户把需求想清楚。

### 第二阶段：PRD 生成

当需求中的主要问题已经澄清，并且用户确认双方理解一致后，将原始材料和多轮对话中确认的内容整理成 `01-prd.md`。

完整流程为：

```text
接收原始需求材料
    ↓
提取已经明确的信息
    ↓
识别模糊、缺失、冲突和隐含决策
    ↓
通过多轮对话逐步追问
    ↓
总结当前需求理解
    ↓
用户确认或修改
    ↓
生成 01-prd.md
```

------

## 3. 基本原则

### 3.1 先理解，再追问

收到需求材料后，先读取和分析其中已有的信息，不要立即开始机械提问。

应先识别：

- 已经明确的内容；
- 描述模糊的内容；
- 缺失但会影响需求实现的内容；
- 材料之间相互冲突的内容；
- AI 当前可能正在默认假设的内容。

已经能够从材料中获得的信息，不要重复询问用户。

------

### 3.2 事实由 Agent 获取，决策由用户确认

Skill 应区分“事实”和“决策”。

事实通常可以从用户提供的文件、图片、代码仓库或已有项目内容中获得，例如：

- 当前项目使用什么技术框架；
- 系统中已经有哪些页面；
- 当前订单有哪些状态；
- 是否已经存在某个功能；
- 当前项目采用什么术语。

这些内容应由 Agent 主动读取和分析，不应要求用户重复说明。

产品决策必须由用户确认，例如：

- 谁可以使用这个功能；
- 哪些状态允许执行某项操作；
- 异常情况下应该如何处理；
- 哪些内容属于本次范围；
- 用户完成操作后应该得到什么结果。

AI 可以提出建议，但不能代替用户作出关键业务决定。

------

### 3.3 采用递进式追问，而不是固定问卷

不要一次性向用户抛出大量固定问题。

应根据当前需求动态建立一个隐性的决策树：

```text
需求目标
├── 使用者是谁
├── 在什么场景下使用
├── 核心操作是什么
│   ├── 前置条件
│   ├── 正常流程
│   └── 操作结果
├── 异常情况
└── 范围边界
```

先询问上层问题。

只有当上层决定明确后，再继续询问依赖它的下层问题。

用户每次回答后，应重新判断：

- 哪些问题已经解决；
- 哪些新问题因为当前回答而产生；
- 下一轮最需要确认什么。

------

### 3.4 每轮只讨论一个主题

为了避免对话变成填写长问卷，每轮应围绕一个主题，询问少量紧密关联的问题。

通常每轮询问 1～3 个问题。

例如可以依次讨论：

1. 需求目标；
2. 用户角色和使用场景；
3. 核心业务流程；
4. 关键业务规则；
5. 异常和边界情况；
6. 需求范围；
7. 验收结果。

不要在第一轮同时询问页面、权限、数据、性能、通知和异常处理等所有内容。

------

### 3.5 问题应附带推荐理解

不要只向用户提出一个完全开放的问题。

每个问题应尽量包含：

- 为什么需要确认这个问题；
- AI 根据当前材料得出的理解；
- AI 推荐的默认方案；
- 用户可以确认、否定或修改的内容。

推荐格式：

```markdown
❓ 需要确认的问题

根据当前需求材料，我理解为：

……

我的建议是：

……

请确认这个理解是否正确，或者直接说明需要调整的地方。
```

例如：

```markdown
❓ 哪些订单状态允许用户取消？

根据当前描述，我理解用户需要在订单发货前取消订单。

我的建议是：
- 待付款订单可以取消；
- 已付款但未发货订单可以取消；
- 已发货订单不允许取消，应进入售后流程。

请确认这个规则是否正确。
```

AI 的建议只是帮助用户思考，不能默认用户已经接受。

------

### 3.6 不接受隐含假设

当某个未确认的决定会明显影响最终需求时，不应静默采用默认值。

例如：

- 谁拥有操作权限；
- 什么状态下允许操作；
- 操作成功后数据如何变化；
- 是否需要通知；
- 是否需要兼容历史数据；
- 某个异常应该阻止操作还是允许继续。

如果 AI 使用了临时假设，应明确告诉用户，并要求确认。

------

### 3.7 避免过度追问

Skill 的目标是形成足够支持后续设计和开发的 PRD，而不是无限追问所有可能情况。

以下内容通常不应在 `/wewo-prd` 阶段深入展开：

- 具体代码如何实现；
- 使用哪个类或函数；
- 数据库字段详细定义；
- 具体接口路径；
- 详细技术架构；
- 测试工具选择；
- 部署方案。

如果用户主动提出技术实现内容，可以记录为约束或参考，但不要让需求澄清过程变成技术设计。

------

## 4. 需要重点澄清的内容

Skill 不需要机械询问所有项目，但应根据需求判断哪些内容需要确认。

### 4.1 需求背景

- 为什么要做这个需求；
- 当前存在什么问题；
- 这个问题对谁造成影响；
- 希望改善什么结果。

### 4.2 需求目标

- 本次需求最终要实现什么；
- 什么结果可以说明需求成功；
- 用户真正想解决的是表面功能还是更深层的问题。

### 4.3 用户和使用场景

- 谁会使用；
- 在什么情况下使用；
- 用户从哪里进入；
- 用户完成操作后希望得到什么。

### 4.4 核心流程

- 操作前需要满足什么条件；
- 用户执行哪些步骤；
- 系统如何响应；
- 操作成功后发生什么。

### 4.5 业务规则

- 哪些情况下允许操作；
- 哪些情况下禁止操作；
- 是否存在状态限制；
- 是否存在角色或权限差异；
- 是否存在次数、数量或时间限制。

### 4.6 异常与边界情况

- 输入为空或不合法时怎么办；
- 重复操作时怎么办；
- 数据不存在时怎么办；
- 状态已经发生变化时怎么办；
- 外部服务失败时用户看到什么；
- 是否有容易被遗漏的特殊情况。

### 4.7 需求范围

必须明确：

- 本次需要完成什么；
- 本次明确不做什么；
- 哪些相关需求留到后续处理。

### 4.8 验收结果

验收标准应描述可以被验证的结果，而不是模糊表述。

避免：

```text
系统应该易用。
功能应该稳定。
页面应该友好。
```

应尽量转化为：

```text
用户提交合法操作后，系统展示成功结果。
不满足操作条件时，系统拒绝请求并说明原因。
重复提交同一操作时，不产生重复业务结果。
```

------

## 5. 对输入材料的处理要求

### 5.1 文本输入

提取：

- 明确需求；
- 关键名词；
- 用户角色；
- 业务动作；
- 限制条件；
- 模糊表达；
- 可能存在的矛盾。

### 5.2 图片输入

分析图片中与需求有关的：

- 页面结构；
- 标注文字；
- 操作入口；
- 状态变化；
- 用户描述的修改位置；
- 图片无法确定的交互细节。

不能只根据截图猜测完整需求。

### 5.3 Office、TXT 和其他文档

读取文件内容后：

- 提取需求信息；
- 合并重复描述；
- 标记相互矛盾的内容；
- 区分已经确定的内容和讨论性内容；
- 不要求用户重新复述文件中已经写明的信息。

### 5.4 多份材料

当用户提供多份文件时，应综合分析。

如果材料之间存在冲突，应明确指出冲突，并让用户确认以哪一个版本为准。

### 5.5 External requirement documents must be opt-in

Do not recursively scan or automatically read arbitrary Markdown files merely
because they exist in the repository.

Use external requirement documents only when at least one of these conditions
is met:

1. The user explicitly references the document.
2. The user explicitly provides a requirement workspace for the current
   requirement, authorizing the documents of that requirement.
3. The user explicitly asks to continue, revise, or update an existing
   requirement.
4. The user uploads or pastes the document in the current interaction.
5. The user explicitly identifies an Issue, task, MR, or document as a source
   for the current requirement.
6. The agent discovers a potentially relevant document and the user
   explicitly confirms it before reading or incorporating it.

A document's existence in a requirement workspace does not by itself
authorize it as input. For a new PRD request, do not automatically read an
existing `01-prd.md` or any other historical requirement document. Do not
scan `docs/wewo/` or the repository looking for previous PRDs or related
requirement documents merely because they appear related.

Repository instruction files such as `AGENTS.md`, `CLAUDE.md`,
`CONTRIBUTING.md`, and relevant `README.md` files may be read automatically
when needed to understand repository conventions, but they MUST NOT be treated
as business requirements unless the user explicitly says so.

If the agent discovers a likely related external requirement document based on
a strong name or path match, it may present that file as a candidate source and
ask the user for confirmation before reading or incorporating it.

The skill MUST NOT:

- recursively read all Markdown files;
- scan `docs/wewo/` or the repository for historical requirement documents;
- read an existing `01-prd.md` for a new PRD request without explicit user
  selection or confirmation;
- select requirement documents only because their content appears similar;
- combine historical or unrelated requirement documents into the current PRD;
- treat repository documentation as confirmed business requirements;
- overwrite or modify external source documents.

External requirement files outside `docs/wewo/...` are read-only input sources.
The generated `01-prd.md` must still be written to the resolved
`docs/wewo/<category>/<slug>/` workspace.

------

## 6. 对话结束条件

在以下情况下，不应生成最终 PRD：

- 核心目标仍不明确；
- 主要使用者仍不明确；
- 核心业务流程仍存在明显冲突；
- 会直接影响功能结果的关键业务规则尚未确认；
- 需求范围仍然模糊；
- 用户还没有确认 AI 对需求的整体理解。

当主要问题已经澄清后，Skill 应先给出一份简洁的需求总结，包括：

- 要解决的问题；
- 目标用户；
- 核心功能；
- 关键业务规则；
- 主要异常情况；
- 本次范围；
- 明确不做的内容。

然后询问用户：

```text
以上是否已经准确表达你的需求？
如果有不准确或遗漏的地方，请直接修改。
确认后我将生成 01-prd.md。
```

只有用户确认后，才生成最终文件。

------

## 7. PRD 文档结构

PRD 采用“固定核心结构 + 动态扩展章节”的方式。

不能完全自由生成，否则不同需求的文档结构会不稳定。

也不能为所有需求强制生成大量无关章节，否则简单需求会变得臃肿。

### 7.1 固定核心结构

`01-prd.md` 至少包含：

```markdown
# 产品需求文档

## 1. 需求概述

## 2. 背景与问题

## 3. 需求目标

## 4. 用户与使用场景

## 5. 需求范围

### 5.1 本次范围

### 5.2 非本次范围

## 6. 功能需求

## 7. 业务规则

## 8. 异常与边界情况

## 9. 验收标准

## 10. 未决问题
```

### 7.2 动态章节

根据实际需求决定是否增加：

- 页面与交互要求；
- 用户角色与权限；
- 数据要求；
- 导入与导出；
- 消息与通知；
- 第三方系统交互；
- 历史数据处理；
- 兼容性要求；
- 性能要求；
- 隐私或合规要求；
- 名词解释；
- 参考资料。

没有涉及的内容不要强行生成。

------

## 8. 文档内容要求

最终 PRD 应满足：

- 只记录用户已经确认的需求；
- 不把 AI 的猜测写成确定需求；
- 使用清晰、准确的业务语言；
- 不写具体代码实现；
- 不提前完成技术设计；
- 功能需求应尽可能明确；
- 业务规则应能够被开发人员理解；
- 验收标准应能够被后续测试；
- 未解决的问题必须保留在“未决问题”中；
- 如果没有未决问题，应明确写“无”。

------

## 9. 输出要求

最终输出文件：

```text
01-prd.md
```

文件必须创建在已经明确解析或确认的独立需求工作区中：

```text
docs/wewo/<requirement-category>/<requirement-slug>/01-prd.md
```

即使项目中存在其他需求文档目录，或读取了位于 `docs/wewo/...` 之外的外部需求文档，也不能把最终 PRD 写入那些位置。外部需求文档仅作为只读输入来源。

生成完成后，应向用户简要说明：

- PRD 文件位置；
- 本次需求的核心目标；
- 是否仍存在未决问题。

不要在生成 PRD 后自动进入技术设计或代码实现阶段。

------

## 10. `/wewo-prd` 不负责的内容

本 Skill 不负责：

- 生成技术设计文档；
- 设计数据库和 ERD；
- 确定接口和详细技术架构；
- 编写实现计划；
- 修改项目代码；
- 生成测试用例；
- 执行测试；
- 进行代码审查。

这些内容由后续 Skill 处理。

`/wewo-prd` 的唯一职责是：

> 将用户提供的不完整原始需求，通过递进式多轮澄清，转化为经过用户确认、能够作为后续设计和开发依据的 `01-prd.md`。
