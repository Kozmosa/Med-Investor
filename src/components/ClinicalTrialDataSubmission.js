import React from 'react';
import { PageHeader, Input, Button } from 'antd';

const ClinicalTrialDataSubmission = () => {
  return (
    <div style={{ padding: '24px' }}>
      <PageHeader
        className="site-page-header"
        title="临床试验数据提交"
      />
      <div style={{ marginTop: '24px' }}>
        <Input.TextArea
          rows={4}
          placeholder="请输入临床试验数据"
          style={{ marginBottom: '16px' }}
        />
        <Button type="primary" style={{ backgroundColor: '#1890ff', borderColor: '#1890ff' }}>
          提交
        </Button>
      </div>
    </div>
  );
};

export default ClinicalTrialDataSubmission;
