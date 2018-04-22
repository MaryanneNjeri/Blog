"""created a relationship

Revision ID: 2bf59c24ffce
Revises: 78d3e29d4656
Create Date: 2018-04-22 14:43:39.680614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bf59c24ffce'
down_revision = '78d3e29d4656'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    op.drop_constraint('posts_comment_id_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'comment_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('posts_comment_id_fkey', 'posts', 'comments', ['comment_id'], ['id'])
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###
