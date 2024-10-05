import React from 'react';
import { Input, Button } from 'antd';
import { LoadingOutlined, SmileOutlined, SolutionOutlined, UserOutlined } from '@ant-design/icons';
import { Steps } from 'antd';

const ClinicalTrialDataSubmission = () => {
  return (
    <div style={{ padding: '24px' }}>
      <header
        className="site-page-header"
        title="临床试验数据提交"
      />
      <Steps
        items={[
          {
            title: 'Login',
            status: 'finish',
            icon: <UserOutlined />,
          },
          {
            title: 'Verification',
            status: 'finish',
            icon: <SolutionOutlined />,
          },
          {
            title: 'Pay',
            status: 'process',
            icon: <LoadingOutlined />,
          },
          {
            title: 'Done',
            status: 'wait',
            icon: <SmileOutlined />,
          },
        ]}
      />
      <div style={{ marginTop: '24px' }}>
        <Input.TextArea
          rows={4}
          placeholder="请输入临床试验数据"
          style={{ marginBottom: '16px' }}
        />

        <Button type="primary">
          提交
        </Button>
      </div>
    </div>
  );
};

export default ClinicalTrialDataSubmission;
