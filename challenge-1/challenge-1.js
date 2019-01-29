const node0 = {val: 0, nodes: []};
const node1 = {val: 1, nodes: []};
const node2 = {val: 2, nodes: []};
const node3 = {val: 3, nodes: []};
const node4 = {val: 4, nodes: []};
const node5 = {val: 5, nodes: []};
const node6 = {val: 6, nodes: []};
const node7 = {val: 7, nodes: []};
const node8 = {val: 8, nodes: []};
const node9 = {val: 9, nodes: []};
const node10 = {val: 10, nodes: []};
const node11 = {val: 11, nodes: []};
const node12 = {val: 12, nodes: []};

node0.nodes = [node1, node10];
node1.nodes = [node0, node2, node11];
node2.nodes = [node1, node3];
node3.nodes = [node2, node4, node5, node6];
node4.nodes = [node3];
node5.nodes = [node3, node6, node7, node8];
node6.nodes = [node3, node8, node9];
node7.nodes = [node5, node9];
node8.nodes = [node5, node6, node9];
node9.nodes = [node6, node7, node8, node10];
node10.nodes = [node0, node12, node9];
node11.nodes = [node1];
node12.nodes = [node10];

const route = [];
const record = [];

function run(node, val) {
    //console.log(node);
    if(record.indexOf(node.val) == -1) {
        record.push(node.val);
        if(node.val == val) {
            return true;
        }
        for (let i = 0; i < node.nodes.length; i++) {
            const nextNode = node.nodes[i];
            if(run(nextNode, val)) {
                route.push(nextNode.val);
                return true;
            }
        }
    }
    return false;
}

run(node0, 6);
route.push(0);
console.log("One route is: ");
console.log(route.reverse());