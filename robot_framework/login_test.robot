*** Settings ***
Suite Teardown    Close All Browsers
Test Teardown
Test Template     ������¼�߼�
Library           Selenium2Library
Resource          resources.robot

*** Test Cases ***
����Ա�û�_��¼�ɹ�
    admin    123456    �˳�

����Ա�û�_��¼ʧ��_������û���
    invalid    123456    �û���������

����Ա�û�_��¼ʧ��_���������
    admin    invalid    �û��������벻ƥ��

*** Keywords ***
������¼�߼�
    [Arguments]    ${username}    ${password}    ${keyword}
    �򿪵�¼ҳ��
    �����û���    ${username}
    ��������    ${password}
    �����¼��ť
    ҳ��Ӧ�ð���    ${keyword}