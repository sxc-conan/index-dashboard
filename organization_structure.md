# 组织架构实体关系设计

## 一、架构分析

根据您提供的组织架构图，系统包含以下层级：
1. **总部** - 最高层级
2. **城市公司** - 区域层级
3. **城市分公司** - 分支层级
4. **主管1** - 管理层级
5. **员工** (Z1-Z7) - 基层员工

## 二、核心设计原则

1. **树形结构**：支持任意层级的组织架构
2. **灵活性**：可以动态添加、删除、重组节点
3. **可扩展性**：支持未来业务变化
4. **职责清晰**：区分组织单元和人员

## 三、实体关系模型（ER模型）

### 3.1 核心实体

#### 实体1: 组织节点 (OrganizationNode)
```
组织节点表 (organization_nodes)
---------------------------------------
id              (主键, UUID/BigInt)
code            (节点编码, 唯一, 如: HQ001, CITY001)
name            (节点名称, 如: 总部、北京分公司)
type            (节点类型: headquarters/city_company/branch/department/team)
level           (层级级别: 1,2,3,4...)
parent_id       (父节点ID, 外键关联自身)
path            (层级路径, 如: /1/12/123/, 便于查询所有子节点)
sort_order      (同级排序)
status          (状态: active/inactive/archived)
attributes      (JSON字段, 存储扩展属性)
created_at      (创建时间)
updated_at      (更新时间)
created_by      (创建人ID)
updated_by      (更新人ID)
```

#### 实体2: 员工/人员 (Employee)
```
员工表 (employees)
---------------------------------------
id              (主键, UUID/BigInt)
employee_no     (工号, 唯一)
name            (姓名)
name_en         (英文名)
gender          (性别)
phone           (电话)
email           (邮箱)
id_card         (身份证号)
hire_date       (入职日期)
resign_date     (离职日期)
status          (状态: active/inactive/resigned)
attributes      (JSON字段, 存储扩展信息)
created_at      (创建时间)
updated_at      (更新时间)
```

#### 实体3: 职位 (Position)
```
职位表 (positions)
---------------------------------------
id              (主键, UUID/BigInt)
code            (职位编码, 唯一)
name            (职位名称, 如: 产品经理、技术总监)
level           (职级: P1-P10, M1-M10)
category        (类别: management/technical/support)
description     (职位描述)
status          (状态: active/inactive)
created_at      (创建时间)
updated_at      (更新时间)
```

#### 实体4: 岗位任职 (EmployeePosition)
```
员工岗位关系表 (employee_positions)
---------------------------------------
id              (主键, UUID/BigInt)
employee_id     (员工ID, 外键)
organization_id (组织节点ID, 外键)
position_id     (职位ID, 外键)
is_primary      (是否主岗位, Boolean)
is_manager      (是否该组织管理者, Boolean)
manager_level   (管理层级: 直接上级/隔级上级等)
effective_date  (生效日期)
expiry_date     (失效日期)
status          (状态: active/inactive)
attributes      (JSON字段, 存储扩展信息)
created_at      (创建时间)
updated_at      (更新时间)
```

#### 实体5: 汇报关系 (ReportingRelationship)
```
汇报关系表 (reporting_relationships)
---------------------------------------
id              (主键, UUID/BigInt)
subordinate_id  (下属员工ID, 外键)
superior_id     (上级员工ID, 外键)
relationship_type (关系类型: direct/dotted/functional)
effective_date  (生效日期)
expiry_date     (失效日期)
status          (状态: active/inactive)
created_at      (创建时间)
updated_at      (更新时间)
```

### 3.2 扩展实体（可选）

#### 实体6: 组织变更历史 (OrganizationChangeLog)
```
组织变更历史表 (organization_change_logs)
---------------------------------------
id              (主键)
change_type     (变更类型: create/update/delete/merge/split)
entity_type     (实体类型: organization/employee/position)
entity_id       (实体ID)
before_data     (变更前数据, JSON)
after_data      (变更后数据, JSON)
change_reason   (变更原因)
effective_date  (生效日期)
operator_id     (操作人ID)
created_at      (创建时间)
```

## 四、关系说明

### 4.1 组织节点自关联
- **关系**: 组织节点 ----< 组织节点
- **类型**: 一对多（自关联）
- **说明**: 通过 parent_id 实现树形结构

### 4.2 员工与组织岗位关系
- **关系**: 员工 ----< 员工岗位关系 >---- 组织节点
- **关系**: 员工 ----< 员工岗位关系 >---- 职位
- **类型**: 多对多（通过中间表）
- **说明**: 一个员工可以在多个组织担任多个职位（兼职场景）

### 4.3 员工汇报关系
- **关系**: 员工 ----< 汇报关系 >---- 员工
- **类型**: 多对多（自关联）
- **说明**: 支持矩阵式管理、虚线汇报等复杂场景

## 五、关系图（ASCII）

```
┌─────────────────────┐
│  OrganizationNode   │
│  (组织节点)          │
└──────────┬──────────┘
           │
           │ parent_id (自关联)
           │
           ↓
    ┌──────────────┐
    │ 子组织节点    │
    └──────────────┘

┌──────────────┐        ┌────────────────────┐        ┌──────────────┐
│   Employee   │◄───────│ EmployeePosition   │───────►│ Organization │
│   (员工)      │        │  (岗位任职)         │        │   Node       │
└──────┬───────┘        └────────┬───────────┘        └──────────────┘
       │                         │
       │                         ↓
       │                ┌──────────────┐
       │                │   Position   │
       │                │   (职位)      │
       │                └──────────────┘
       │
       │ ┌────────────────────────┐
       └─│ ReportingRelationship  │
         │   (汇报关系)            │
         └────────────────────────┘
```

## 六、核心查询场景

### 6.1 查询某个节点的所有子节点（递归查询）
```sql
-- 使用 path 字段快速查询
SELECT * FROM organization_nodes 
WHERE path LIKE '/1/12/%';

-- 或使用递归 CTE
WITH RECURSIVE org_tree AS (
    SELECT * FROM organization_nodes WHERE id = :parent_id
    UNION ALL
    SELECT n.* FROM organization_nodes n
    INNER JOIN org_tree t ON n.parent_id = t.id
)
SELECT * FROM org_tree;
```

### 6.2 查询员工的完整组织路径
```sql
SELECT 
    e.name AS employee_name,
    p.name AS position_name,
    o.name AS organization_name,
    o.path AS org_path
FROM employees e
JOIN employee_positions ep ON e.id = ep.employee_id
JOIN positions p ON ep.position_id = p.id
JOIN organization_nodes o ON ep.organization_id = o.id
WHERE e.id = :employee_id AND ep.status = 'active';
```

### 6.3 查询某组织下的所有员工（包括子组织）
```sql
SELECT DISTINCT e.*
FROM employees e
JOIN employee_positions ep ON e.id = ep.employee_id
JOIN organization_nodes o ON ep.organization_id = o.id
WHERE o.path LIKE '/1/12/%' 
  AND ep.status = 'active'
  AND e.status = 'active';
```

### 6.4 查询员工的直接上级
```sql
SELECT 
    e_sup.name AS superior_name,
    p.name AS position_name
FROM employees e
JOIN reporting_relationships rr ON e.id = rr.subordinate_id
JOIN employees e_sup ON rr.superior_id = e_sup.id
LEFT JOIN employee_positions ep ON e_sup.id = ep.employee_id AND ep.is_primary = true
LEFT JOIN positions p ON ep.position_id = p.id
WHERE e.id = :employee_id 
  AND rr.status = 'active'
  AND rr.relationship_type = 'direct';
```

## 七、灵活性设计要点

### 7.1 支持多种组织结构
- **职能型**: 按部门划分（研发部、市场部）
- **区域型**: 按地域划分（华北区、华东区）
- **矩阵型**: 员工可同时属于多个组织
- **项目型**: 临时项目组

### 7.2 历史版本管理
- 使用 `effective_date` 和 `expiry_date` 实现时间维度
- 保留历史记录，支持查询任意时间点的组织结构

### 7.3 扩展属性
- 使用 JSON 字段存储个性化属性
- 避免频繁修改表结构

### 7.4 软删除
- 使用 `status` 字段而非物理删除
- 保留数据完整性

## 八、实现建议

### 8.1 技术栈建议
- **数据库**: PostgreSQL（支持递归查询、JSON字段）
- **ORM**: SQLAlchemy / Django ORM
- **缓存**: Redis（缓存组织树结构）

### 8.2 性能优化
- 为 `path` 字段添加索引（B-tree）
- 为 `parent_id` 添加索引
- 定期归档历史数据
- 使用物化视图缓存常用查询

### 8.3 数据一致性
- 添加外键约束
- 使用数据库事务
- 添加唯一约束防止重复

## 九、扩展功能

1. **权限管理**: 基于组织的权限控制
2. **审批流**: 按组织层级配置审批流程
3. **数据权限**: 限制用户只能看到所属组织的数据
4. **组织画像**: 统计分析各组织的人员、绩效等指标
5. **继任计划**: 关键岗位的人才储备


