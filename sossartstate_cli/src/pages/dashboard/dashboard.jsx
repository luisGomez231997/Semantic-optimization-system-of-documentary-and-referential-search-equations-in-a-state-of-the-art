import React, { useState } from "react";
import { Layout, Menu, Avatar } from "antd";
import Css from "./dashboard";
import {
  PieChartOutlined,
  UserOutlined,
  BookOutlined,
  DatabaseOutlined,
} from "@ant-design/icons";
import logo from "../../assests/icons/logo.svg";

const { Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;

function Dashboard(props) {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={Css.layout_main}>
      <Sider
        style={Css.sider}
        collapsible
        collapsed={collapsed}
        onCollapse={() => setCollapsed(!collapsed)}
      >
        <Avatar src={logo} />
        <Menu mode="inline">
          <SubMenu key="accountU" icon={<UserOutlined />} title="User Account">
            <Menu.Item key="accountU-1">Profile</Menu.Item>
            <Menu.Item key="accountU-2">Configuration</Menu.Item>
            <Menu.Item key="accountU-3">Log-Out</Menu.Item>
          </SubMenu>
          <SubMenu
            key="knowledgeG"
            icon={<PieChartOutlined />}
            title="Knowledge Graphs"
          >
            <Menu.Item key="knowledgeG-1">Histoty Graph</Menu.Item>
            <Menu.Item key="knowledgeG-2">Relation K-words</Menu.Item>
            <Menu.Item key="knowledgeG-3">Wide Area</Menu.Item>
          </SubMenu>
          <SubMenu
            key="equationsB"
            icon={<BookOutlined />}
            title="Equations Book"
          >
            <Menu.Item key="equationsB-1">Write Equations</Menu.Item>
            <Menu.Item key="equationsB-2">Assemble Equations</Menu.Item>
          </SubMenu>
          <SubMenu
            key="knowledgeB"
            icon={<DatabaseOutlined />}
            title="Knowledge Base"
          >
            <Menu.Item key="knowledgeB-1">Data Store</Menu.Item>
          </SubMenu>
        </Menu>
      </Sider>
      <Layout className="site-layout">
        <Content style={Css.content_footer}></Content>
        <Footer style={Css.footer}>
          Luis A. Gómez © 2021 All right are reserved.
        </Footer>
      </Layout>
    </Layout>
  );
}

export default Dashboard;
